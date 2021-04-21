@echo off
SETLOCAL ENABLEDELAYEDEXPANSION

rem Set values for your storage account
set subscription_id=b9936f95-44b4-433d-be79-5a3db7765380
set azure_storage_account=azsademo
set azure_storage_key=5zTVq3aPUzlgniFqjqUDxekaIlrSfWbCauOKF00EQsbTgzYqEVdLKz+QcNs5J80tBcYcKeSJN/0ov2OeHJ89AQ==


echo Creating container...
call az storage container create --account-name azsademo --subscription !subscription_id! --name margies --public-access blob --auth-mode key --account-key 5zTVq3aPUzlgniFqjqUDxekaIlrSfWbCauOKF00EQsbTgzYqEVdLKz+QcNs5J80tBcYcKeSJN/0ov2OeHJ89AQ== --output none

echo Uploading files...
call az storage blob upload-batch -d margies -s data --account-name azsademo --auth-mode key --account-key 5zTVq3aPUzlgniFqjqUDxekaIlrSfWbCauOKF00EQsbTgzYqEVdLKz+QcNs5J80tBcYcKeSJN/0ov2OeHJ89AQ==  --output none