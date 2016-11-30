# parses response from google calendar api call
import json

def parse_from_google_response(response):
  loaded_data = json.loads(response.replace('""', '"'))
  return compose_output_from_google_response(loaded_data["items"])
  
def compose_output_from_google_response(events):
  output = "["
  for event in events:
    output += "{\"name\": \"%s\", \"start_date\": \"%s\",\"end_date\": \"%s\", \"status\": \"%s\"}" % (event["summary"], get_date_from_google_event(event, "start"), get_date_from_google_event(event, "end"), event["status"])
    if event != events[-1]:
      output += ","
  return output + "]"

def get_date_from_google_event(event, date_type):
  if 'dateTime' not in event[date_type]:
    return event[date_type]['date']
  return event[date_type]['dateTime']
  
# parses response for google calendar api call
def compose_google_request(events):
  loaded_data = json.loads(events)
  return compose_output_for_google_request(loaded_data)

def compose_output_for_google_request(data):
  output = ""
  for event in data:
    output += "{\"start\": %s,\"end\": %s,\"summary\": \"%s\"}" % (get_date_for_google_event(event, 'start_date'), get_date_for_google_event(event, 'end_date'), event['name'])
    if event != data[-1]:
      output += ","
  return output
  
def get_date_for_google_event(event, date_type):
  if 'T' not in event[date_type]:
    return "{ \"date\": \"" + event[date_type] + "\"}"
  return "{ \"dateTime\": \"" + event[date_type] + "\"}"
