
import os
from PIL import Image

IMG_SIZE = (224, 224)

def preprocess_dataset(
    input_dir, output_dir ):

    os.makedirs(
        output_dir, exist_ok=True )

    classes = os.listdir( input_dir)

    for cls in classes:

        input_class = os.path.join(
            input_dir, cls)

        if not os.path.isdir(
            input_class):
            continue

        output_class = os.path.join(
            output_dir, cls )

        os.makedirs(
            output_class, exist_ok=True )

        for image_name in os.listdir(
            input_class ):

            image_path = os.path.join(
                input_class, image_name )

            try:

                img = Image.open( image_path )

                img = img.convert( "RGB" )

                img = img.resize( IMG_SIZE )

                save_path = os.path.join(
                    output_class, image_name )

                img.save( save_path )

            except Exception as e:

                print(
                    f"Gagal memproses {image_name}: {e}"
                )

    print(
        "Preprocessing selesai."
    )

if __name__ == "__main__":

    preprocess_dataset(
        "/content/drive/MyDrive/Eksperimen_SML_Aulia Silmi Mardiyanti/mango_dataset",
        "/content/drive/MyDrive/Eksperimen_SML_Aulia Silmi Mardiyanti/preprocessing/mango_preprocessing"
    )
