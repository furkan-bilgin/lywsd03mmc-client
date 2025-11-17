from lywsd03mmc.lywsd03mmc_client import Lywsd03mmcClientSyncContext, Lywsd03mmcData

MAC_ADDRESS_OR_UUID = 'A4:C1:38:AE:DB:73'

while True:
    try:
        with Lywsd03mmcClientSyncContext(MAC_ADDRESS_OR_UUID, timeout_sec=60) as client:
            data: Lywsd03mmcData = client.get_data()
            print(data)
    except Exception as ex:
        print(f"Error: {ex}")
