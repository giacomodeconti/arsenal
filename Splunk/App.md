# Create an App in Splunk
## Windows or linux is same
### Creation
1. Open directory apps `/opt/splunkforwarder/etc/apps/` in Windows is under ProgramFiles
2. Create the app with `mkdir app_test`
3. Go inside and make another two folders `local` and `metadata`
4. In `local` create inputs.conf and outputs.conf
5. In `metadata` create local.meta
    - `local.meta` :
      ```
      []
      access = read : [ * ], write : [ admin ]
      export = system
      ```
6. Should look this
    ```
    └── app_test
        ├── local
        │   ├── inputs.conf
        │   └── outputs.conf
        └── metadata
            └── local.meta
    ```

