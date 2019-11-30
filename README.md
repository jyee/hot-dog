# Hot Dog!

This is a stupid demo app that shows a couple dog photos. Choose the one you like. It will keep showing pairs of dogs and when you like a dog 3 times, it will save that dog photo for you.

## Stupider

The front end is designed to run in Kubernetes.
The save function is an AWS lambda function that will take the image url, fetch the image, and save it to an s3 bucket.
