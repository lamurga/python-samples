from PIL import Image
import os
from django.conf import settings

def upload_s3(filename, fn, filetype, name):
    success = False
    try:
        from boto.s3.key import Key
        from boto.s3.connection import S3Connection

        conn = S3Connection(settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY)
        bucket = conn.get_bucket(settings.AWS_STORAGE_BUCKET_NAME)

        if filename and fn and filetype and name:
            if 'image' == filetype:
                image = Image.open(filename)
                image.save(fn, image.format)
            else:
                destination = open(fn, 'wb+')
                for chunk in filename.chunks():
                    destination.write(chunk)
                destination.close()

            k = Key(bucket)
            k.key = name
            k.set_contents_from_filename(fn)
            k.make_public()
            os.remove(fn)
            success = True

    except Exception, e:
        print e
        pass

    return success