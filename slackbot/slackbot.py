from slackclient import SlackClient
import time

slack_client = SlackClient("xoxb-284699092677-U436fZDs69owqVvPhhMPDBkI")

if slack_client.rtm_connect(with_team_state=False):
    print
    "Successfully connected, listening for events"
    while True:
        print(slack_client.rtm_read())

        time.sleep(1)
else:
    print("Connection Failed")