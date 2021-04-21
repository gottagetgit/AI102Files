@echo off
SETLOCAL ENABLEDELAYEDEXPANSION

rem Set values for your storage account
set subscription_id=YourSubscriptionID
set azure_storage_account=YourStorageAccountName
set azure_storage_key=YourStorageKey


echo Creating container...
call az storage container create --account-name azsademo --subscription !subscription_id! --name margies --public-access blob --auth-mode key --account-key 5zTVq3aPUzlgniFqjqUDxekaIlrSfWbCauOKF00EQsbTgzYqEVdLKz+QcNs5J80tBcYcKeSJN/0ov2OeHJ89AQ== --output none

echo Uploading files...
call az storage blob upload-batch -d margies -s data --account-name azsademo --auth-mode key --account-key 5zTVq3aPUzlgniFqjqUDxekaIlrSfWbCauOKF00EQsbTgzYqEVdLKz+QcNs5J80tBcYcKeSJN/0ov2OeHJ89AQ==  --output none