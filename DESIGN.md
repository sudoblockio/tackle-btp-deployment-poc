
###  Users 

- Cyrus
  - Prod 
  - Needs 
    - Secure easy deployment 
    - Will have access to keystores 
- Developers 
  - Dev / Testing 
  - Needs 
    - Shared access to keystores
- GitHub Actions 
  - Automation 
  - Needs 


### Actions

- Build
  - Output
    - Artifact
- Deployment -> Provisioning 
  - Input 
    - Artifact
    - Keystore
  - Output
    - Address
- Provisioning -> Configuration
  - Input 
    - Keystore + Address 


### Key Management 

- [ ] POCs
