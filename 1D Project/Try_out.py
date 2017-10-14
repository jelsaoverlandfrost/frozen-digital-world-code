# [START import_libraries]
import argparse
import base64

import googleapiclient.discovery


# [END import_libraries]


def main(photo_file):
    """Run a label request on a single image"""

    # [START authenticate]
    API_KEY = 'AIzaSyB1WDZ72d9bLdsI_RbE34zWzYhAKObUo_8'
    service = googleapiclient.discovery.build('vision', 'v1', developerKey=API_KEY)
    # [END authenticate]

    # [START construct_request]
    with open(photo_file, 'rb') as image:
        image_content = base64.b64encode(image.read())
        service_request = service.images().annotate(body={
            'requests': [{
                'image': {
                    'content': image_content.decode('UTF-8')
                },
                'features': [{
                    'type': 'LABEL_DETECTION',
                    'maxResults': 5
                }]
            }]
        })
        # [END construct_request]
        # [START parse_response]
        response = service_request.execute()
        for results in response['responses']:
            if 'labelAnnotations' in results:
                for annotations in results['labelAnnotations']:
                    print('Found label %s, score = %s' % (annotations['description'], annotations['score']))
        # [END parse_response]


# [START run_application]
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('image_file', help='The image you\'d like to label.')
    args = parser.parse_args()
    main(args.image_file)
    # [END run_application]
