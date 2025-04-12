# CS50 assignment: implement a program that prompts the user for the name of a file and 
# then outputs that file’s media type if the file’s name ends, case-insensitively, in 
# any of these suffixes:

#    .gif
#    .jpg
#    .jpeg
#    .png
#    .pdf
#    .txt
#    .zip

def main():
    filename = input("Type the name and file extension: ").strip().lower().split('.')
    filename = filename[-1]
    print(find_mediatype(filename))

    # alt solution using dict:
    print(alt_find_mediatype(filename))

def find_mediatype(f):
    match f:
        case "gif":
            return "image/gif"
        case "jpg" | "jpeg":
            return "image/jpeg"
        case "png":
            return "image/png"
        case "pdf":
            return "application/pdf"
        case "txt":
            return "text/plain"
        case "zip":
            return "application/zip"
        
# alternative solution, using dict:

extensions = {
    "gif":"image/gif",
    "jpg":"image/jpeg",
    "jpeg":"image/jpeg",
    "png":"image/png",
    "pdf":"application/pdf",
    "txt":"text/plain",
    "zip":"application/zip"
    }
        
def alt_find_mediatype(f):
    for extension in extensions:
        if f == extension:
            return(extensions[extension])
        
main()
