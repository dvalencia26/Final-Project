from clarifai.client.user import User
client = User(user_id="learn_ai_04", pat="5475a50c9c494d20aadc975e33e29733")

# Get all apps
apps_generator = client.list_apps()
apps = list(apps_generator)

print(apps)


##################################################################################################
# In this section, we set the user authentication, user and app ID, model details, and the URL
# of the image we want as an input. Change these strings to run your own example.
#################################################################################################

# Your PAT (Personal Access Token) can be found in the portal under Authentification
PAT = '5475a50c9c494d20aadc975e33e29733'
# Specify the correct user_id/app_id pairings
# Since you're making inferences outside your app's scope
USER_ID = 'learn_ai_04'
APP_ID = 'face_detection'
# Change these to whatever model and image URL you want to use
MODEL_ID = 'face-detection'
MODEL_VERSION_ID = '6dc7e46bc9124c5c8824be4822abe105'
IMAGE_URL = 'https://samples.clarifai.com/metro-north.jpg'

############################################################################
# YOU DO NOT NEED TO CHANGE ANYTHING BELOW THIS LINE TO RUN THIS EXAMPLE
############################################################################

from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import resources_pb2, service_pb2, service_pb2_grpc
from clarifai_grpc.grpc.api.status import status_code_pb2


def face_detection_ai(path):

    channel = ClarifaiChannel.get_grpc_channel()
    stub = service_pb2_grpc.V2Stub(channel)

    metadata = (('authorization', 'Key ' + PAT),)

    userDataObject = resources_pb2.UserAppIDSet(user_id=USER_ID, app_id=APP_ID)
    with open(path, "rb") as f:
        file_bytes = f.read()
    post_model_outputs_response = stub.PostModelOutputs(
        service_pb2.PostModelOutputsRequest(
            user_app_id=userDataObject,  # The userDataObject is created in the overview and is required when using a PAT
            model_id=MODEL_ID,
            version_id=MODEL_VERSION_ID,  # This is optional. Defaults to the latest model version
            inputs=[
                resources_pb2.Input(
                    data=resources_pb2.Data(
                        image=resources_pb2.Image(
                            base64=file_bytes
                        )
                    )
                )
            ]
        ),
        metadata=metadata
    )
    if post_model_outputs_response.status.code != status_code_pb2.SUCCESS:
        print(post_model_outputs_response.status)
        raise Exception("Post model outputs failed, status: " + post_model_outputs_response.status.description)

    # Since we have one input, one output will exist here
    output = post_model_outputs_response.outputs[0]
    print(output)
    has_face = False

    for region in output.data.regions:
        if region.value > float(.6):
            has_face = True
            print(region.value)

    print("This image contains a Face " + str(has_face))
    return has_face
# Uncomment this line to print the full Response JSON
#print(output)

