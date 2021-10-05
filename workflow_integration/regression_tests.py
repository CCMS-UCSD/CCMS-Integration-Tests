from numpy.core.numeric import outer
import pandas as pd
import argparse
import time
import requests

def test_view_counts(old_task_id, new_task_id, server_url, view_name):
    print(old_task_id, new_task_id, server_url, view_name)

    old_url = "https://{}/ProteoSAFe/result_json.jsp?task={}&view={}".format(server_url, old_task_id, view_name)
    new_url = "https://{}/ProteoSAFe/result_json.jsp?task={}&view={}".format(server_url, new_task_id, view_name)

    old_data = requests.get(old_url).json()["blockData"]
    new_data = requests.get(new_url).json()["blockData"]

    if isinstance(old_data, list):
        # JSON list, client side results
        old_df = pd.DataFrame(old_data)
        new_df = pd.DataFrame(new_data)
        if len(old_df) == len(new_df):
            return True
        else:
            return False
    else:
        # Let's sleep and try to get the data again
        time.sleep(5)

        old_url = "https://{}/ProteoSAFe/result_json.jsp?task={}&view={}".format(server_url, old_task_id, view_name)
        new_url = "https://{}/ProteoSAFe/result_json.jsp?task={}&view={}".format(server_url, new_task_id, view_name)

        old_data = requests.get(old_url).json()["blockData"]
        new_data = requests.get(new_url).json()["blockData"]

        # Server side results
        old_count = old_data["total_rows"]
        new_count = new_data["total_rows"]

        if old_count == new_count:
            return True
        else:
            return False

    