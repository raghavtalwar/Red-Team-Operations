class JsonFlattener:
    import json  # Importing the json module

    def __init__(self, message_info):
        self.message_info = message_info

    def flatten_json(self, json_obj, parent_key='', sep='_'):
        items = {}
        for k, v in json_obj.iteritems():
            new_key = parent_key + sep + k if parent_key else k
            if isinstance(v, dict):
                items.update(self.flatten_json(v, new_key, sep=sep))
            else:
                items[new_key] = v
        return items

    def traverse_flattened_json(self, flattened_json, target_key):
        results = []
        for key, value in flattened_json.items():
            if key == target_key:
                results.append(value)
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        results.extend(self.traverse_flattened_json(item, target_key))
            elif isinstance(value, dict):
                results.extend(self.traverse_flattened_json(value, target_key))
        return results

    def process_response(self):
        response_info = helpers.analyzeResponse(self.message_info.getResponse())
        headers = response_info.getHeaders()
        msgResponseBody = self.message_info.getResponse()[response_info.getBodyOffset():]
        msg = helpers.bytesToString(msgResponseBody)

        try:
            # Parse JSON response
            json_response = self.json.loads(msg)  # Using self.json to refer to the imported json module
            # print("Original JSON response:")
            # print(json_response)

            # Flatten JSON
            flattened_json = self.flatten_json(json_response)
            # print("\nFlattened JSON:")
            # print(flattened_json)

            # Traverse flattened JSON to fetch the value of 'objectType' key dynamically
            object_types = self.traverse_flattened_json(flattened_json, 'objectType')
            unique_object_types = set(object_types)

            if unique_object_types:
                print("\nUnique value(s) of 'objectType' key found dynamically:")
                for obj_type in unique_object_types:
                    print(obj_type)
            else:
                print("\n")
        except Exception as e:
            pass
            #print("Error parsing JSON response:", e)

# Example usage:
enabled = True
if not messageIsRequest and enabled:
    json_flattener = JsonFlattener(messageInfo)
    json_flattener.process_response()
