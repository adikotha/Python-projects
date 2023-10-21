import cv2

def process_photo(photo_file):
    try:
        # Read the input photo file
        photo = cv2.imread(photo_file)

        if photo is not None:
            # Perform actions on the photo here
            # For example, you can display the photo or apply image processing.

            # Display the photo (you can remove this if not needed)
            cv2.imshow('Input Photo', photo)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

            # You can add your own processing steps here

        else:
            print("Error: Could not read the photo file.")

    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    try:
        # Prompt the user to enter the file path of the photo
        photo_file = input("Enter the file path of the photo: ")
        
        # Call the function to process the photo
        process_photo(photo_file)

    except KeyboardInterrupt:
        print("Operation aborted by the user.")

if __name__ == "__main__":
    main()
