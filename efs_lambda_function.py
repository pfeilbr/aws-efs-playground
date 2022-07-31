
import os
import json
efs_mount_path = '/mnt/efs'

def lambda_handler(event, context):
    print("Hello, world!")
    output = ""
    if os.path.exists(efs_mount_path):
        f = open(f"{efs_mount_path}/a.txt", "a")
        f.write("hello from lambda")
        f.close()
        output = f"{efs_mount_path} contents\n\n{os.listdir(efs_mount_path)}"
        print(output)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "output": output
        }),
    }


