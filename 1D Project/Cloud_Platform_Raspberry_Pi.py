# [START import_libraries]
import base64
import googleapiclient.discovery
from time import sleep
# from picamera import PiCamera
from firebase import firebase
from google.cloud import storage

# [END import_libraries]

# Initializing PiCamera
# camera = PiCamera()

# Initializing Firebase
token = 'LQdeuWHXvtgCg5Sdx3JUfuGV1ZaUmfbA7Nah5hE3'
url = 'https://dmini-internet-of-things.firebaseio.com/'
firebase = firebase.FirebaseApplication(url, token)


def storing(photo_file):
    client = storage.Client()
    bucket = client.get_bucket('frozenfrosty')
    blob = bucket.blob('frozen')
    blob.upload_from_filename(filename=photo_file)
    print("Stored!")


def main(photo_file):
    """Run a label request on a single image"""

    # [START authenticate]
    API_KEY = 'AIzaSyBIAARIMAia2tBhxKMYVntl4WbnAlhUdKc'
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

        # Return the response
        response = service_request.execute()
        result = {}
        for results in response['responses']:
            if 'labelAnnotations' in results:
                for annotations in results['labelAnnotations']:
                    result[annotations['description']] = annotations['score']
        return result


# def photoTaking():
#     camera.start_preview(alpha=100)
#     camera.capture('/home/pi/Desktop/image.jpg')
#     camera.stop_preview()


# [START run_application]
if __name__ == '__main__':
    while True:
        # photoTaking()
        finalResult = main('/Users/frozen/Downloads/IMG_0191.jpg')
        # Update the result to firebasea
        firebase.put('/results', '/', finalResult)
        print('successfully put into firebase')
        # Upload the image
        storing('/Users/frozen/Downloads/IMG_0191.jpg')
        # Snooze for 3 seconds to wait for the request to be shown
        sleep(3)
# [END run_application]
