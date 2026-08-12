import bson
import json
import os
from bson import ObjectId
from datetime import datetime


class BSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        if isinstance(obj, datetime):
            return obj.isoformat()  # Convert datetime to ISO format string
        return super().default(obj)


folder = r"C:\Users\alnur\Downloads\quick-mongo-atlas-datasets-master\quick-mongo-atlas-datasets-master\dump\sample_training"

for file in os.listdir(folder):
    if file.endswith('.bson'):
        collection_name = file.replace('.bson', '')
        bson_file = os.path.join(folder, file)
        json_file = os.path.join(folder, f"{collection_name}_data.json")

        print(f"Converting {file}...")
        try:
            with open(bson_file, 'rb') as f:
                data = list(bson.decode_file_iter(f))
                with open(json_file, 'w') as out:
                    json.dump(data, out, cls=BSONEncoder)
            print(f"✓ Created {collection_name}_data.json")
        except Exception as e:
            print(f"✗ Error: {e}")

print("All done!")