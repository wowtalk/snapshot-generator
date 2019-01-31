import boto3

STREAM_NAME = "wowtalk-android"
kvs = boto3.client(
    "kinesisvideo",
    region_name='eu-west-1'
)

# Grab the endpoint from GetDataEndpoint
endpoint = kvs.get_data_endpoint(
    APIName="GET_HLS_STREAMING_SESSION_URL",
    StreamName=STREAM_NAME
)['DataEndpoint']
# Grab the HLS Stream URL from the endpoint
kvam = boto3.client("kinesis-video-archived-media",
    aws_access_key_id='AKIAJUCTYSWYTW4BNB4A',
    aws_secret_access_key='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',
    region_name='eu-west-1',
    endpoint_url=endpoint)

url = kvam.get_hls_streaming_session_url(
    StreamName=STREAM_NAME,
    PlaybackMode="LIVE"
)['HLSStreamingSessionURL']
print(url)
