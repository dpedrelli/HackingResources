# DLL Search Order
1) Directory from which application launched
2) C:\Windows\System32
3) C:\Windows\System
4) C:\Windows
5) Current directory
6) Directories specified in the environment %PATH% variable.

# Steps To Execute
1) Create a filter for a specific EXE to investigate.
2) Create a filter for NAME NOT FOUND, for the Result column.
3) Look for instances that the application is looking for a DLL in a directory for which we have write permissions.
4) Copy payload (modified DLL) into a writable directory.
5) Restart service.

# References
##### [Dynamic-Link Library Search Order](https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-search-order?redirectedfrom=MSDN)
##### [Secure loading of libraries to prevent DLL preloading attacks](https://support.microsoft.com/en-us/topic/secure-loading-of-libraries-to-prevent-dll-preloading-attacks-d41303ec-0748-9211-f317-2edc819682e1)