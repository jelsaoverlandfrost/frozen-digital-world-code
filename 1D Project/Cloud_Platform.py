# # [START import_libraries]
# import base64
# #import googleapiclient.discovery
# from time import sleep
# #from google.cloud import storage
# # [END import_libraries]
#
#
# def main(photo_file):
#     """Run a label request on a single image"""
#
#     # [START authenticate]
#     API_KEY = 'AIzaSyBIAARIMAia2tBhxKMYVntl4WbnAlhUdKc'
#     service = googleapiclient.discovery.build('vision', 'v1', developerKey=API_KEY)
#     # [END authenticate]
#
#     # [START construct_request]
#     with open(photo_file, 'rb') as image:
#         image_content = base64.b64encode(image.read())
#         service_request = service.images().annotate(body={
#             'requests': [{
#                 'image': {
#                     'content': image_content.decode('UTF-8')
#                 },
#                 'features': [{
#                     'type': 'LABEL_DETECTION',
#                     'maxResults': 5
#                 }]
#             }]
#         })
#         # [END construct_request]
#         response = service_request.execute()
#         for results in response['responses']:
#             if 'labelAnnotations' in results:
#                 for annotations in results['labelAnnotations']:
#                     print('Found label %s, score = %s' % (annotations['description'], annotations['score']))
#
#
# # [START run_application]
# if __name__ == '__main__':
#     while True:
#         main('/Users/frozen/Downloads/IMG_0191.jpg')
#         print 'Start Snoozing'
#         # Snooze for 10 seconds to refresh the image
#
#         sleep(10)
# # [END run_application]
