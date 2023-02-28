#!/bin/sh
# SPDX-FileCopyrightText: 2021 Splunk, Inc. <sales@splunk.com>
# SPDX-License-Identifier: Apache-2.0

# shellcheck disable=SC1091
. "$(dirname "$0")"/common.sh

HEADER='CPU    pctUser    pctNice  pctSystem  pctIowait    pctIdle'
HEADERIZE="BEGIN {print \"$HEADER\"}"
PRINTF='{printf "%-3s  %9s  %9s  %9s  %9s  %9s\n", cpu, pctUser, pctNice, pctSystem, pctIowait, pctIdle}'

if [ "$KERNEL" = "Linux" ] ; then
    queryHaveCommand sar
    FOUND_SAR=$?
    queryHaveCommand mpstat
    FOUND_MPSTAT=$?
    if [ $FOUND_SAR -eq 0 ] ; then
        CMD='sar -P ALL 1 1'
        # shellcheck disable=SC2016
        FORMAT='{cpu=$(NF-6); pctUser=$(NF-5); pctNice=$(NF-4); pctSystem=$(NF-3); pctIowait=$(NF-2); pctIdle=$NF}'
    elif [ $FOUND_MPSTAT -eq 0 ] ; then
        CMD='mpstat -P ALL 1 1'
        # shellcheck disable=SC2016
        FORMAT='{cpu=$(NFIELDS-10); pctUser=$(NFIELDS-9); pctNice=$(NFIELDS-8); pctSystem=$(NFIELDS-7); pctIowait=$(NFIELDS-6); pctIdle=$NF}'
    else
        failLackMultipleCommands sar mpstat
    fi
    # shellcheck disable=SC2016
    FILTER='($0 ~ /CPU/) { if($(NF-1) ~ /gnice/){  NFIELDS=NF; } else {NFIELDS=NF+1;} next} /Average|Linux|^$|%/ {next}'
elif [ "$KERNEL" = "SunOS" ] ; then
    if [ "$SOLARIS_8" = "true" ] || [ "$SOLARIS_9" = "true" ] ; then
        CMD='eval mpstat -a -p 1 2 | tail -1 | sed "s/^[ ]*0/all/"; mpstat -p 1 2 | tail -r'
    else
        CMD='eval mpstat -aq -p 1 2 | tail -1 | sed "s/^[ ]*0/all/"; mpstat -q -p 1 2 | tail -r'
    fi
    assertHaveCommand "$CMD"
    # shellcheck disable=SC2016
    FILTER='($1=="CPU") {exit 1}'
    # shellcheck disable=SC2016
    FORMAT='{cpu=$1; pctUser=$(NF-4); pctNice="0"; pctSystem=$(NF-3); pctIowait=$(NF-2); pctIdle=$(NF-1)}'
elif [ "$KERNEL" = "AIX" ] ; then
    queryHaveCommand sar
    FOUND_SAR=$?
    if [ $FOUND_SAR -eq 0 ] ; then
        CMD='sar -P ALL 1 1'
    # shellcheck disable=SC2016
    FORMAT='{k=0;if(NR==7) k=1} {sub("^-", "all", $1); cpu=$(1+k); pctUser=$(2+k); pctNice="0"; pctSystem=$(3+k); pctIowait=$(4+k); pctIdle=$(5+k)}'
    fi
    FILTER='/System|AIX|^$|%/ {next}'
elif [ "$KERNEL" = "Darwin" ] ; then
    HEADER='CPU    pctUser  pctSystem    pctIdle'
    HEADERIZE="BEGIN {print \"$HEADER\"}"
    PRINTF='{printf "%-3s  %9s  %9s  %9s \n", cpu, pctUser, pctSystem, pctIdle}'
    # top command here is used to get a single instance of cpu metrics
    CMD='top -l 1'
    assertHaveCommand "$CMD"
    # FILTER here skips all the rows that doesn't match "CPU".
    # shellcheck disable=SC2016
    FILTER='($1 !~ "CPU") {next;}'
    # FORMAT here removes '%'in the end of the metrics.
    # shellcheck disable=SC2016
    FORMAT='function remove_char(string, char_to_remove) {
                                    sub(char_to_remove, "", string);
                                    return string;
                            }
                            {
                                cpu="all";
                                pctUser = remove_char($3, "%");
                                pctSystem = remove_char($5, "%");
                                pctIdle = remove_char($7, "%");
                                }'
elif [ "$KERNEL" = "FreeBSD" ] ; then
    CMD='eval top -P -d2 c; top -d2 c'
    assertHaveCommand "$CMD"
    # shellcheck disable=SC2016
    FILTER='($1 !~ "CPU") { next; }'
    # shellcheck disable=SC2016
    FORMAT='function remove_char(string, char_to_remove) {
				sub(char_to_remove, "", string);
				return string;
			}
			{
				if ($1 == "CPU:") {
					cpu = "all";
				} else {
					cpu = remove_char($2, ":");
				}
			}
			{
				pctUser = remove_char($(NF-9), "%");
				pctNice = remove_char($(NF-7), "%");
				pctSystem = remove_char($(NF-5), "%");
				pctIdle = remove_char($(NF-1), "%");
				pctIowait = "0.0";
			}'
elif [ "$KERNEL" = "HP-UX" ] ; then
    queryHaveCommand sar
    FOUND_SAR=$?
    if [ $FOUND_SAR -eq 0 ] ; then
        CMD='sar -M 1 1 ALL'
    fi
    FILTER='/HP-UX|^$|%/ {next}'
    # shellcheck disable=SC2016
    FORMAT='{k=0; if(5<NF) k=1} {cpu=$(1+k); pctUser=$(2+k); pctNice="0"; pctSystem=$(3+k); pctIowait=$(4+k); pctIdle=$(5+k)}'
fi

$CMD | tee "$TEE_DEST" | $AWK "$HEADERIZE $FILTER $FORMAT $PRINTF"  header="$HEADER"
echo "Cmd = [$CMD];  | $AWK '$HEADERIZE $FILTER $FORMAT $PRINTF' header=\"$HEADER\"" >> "$TEE_DEST"
