from file_generation import static_to_public, generate_page

def main():
    static_to_public("./static", './public')
    generate_page('content/index.md', 'template.html', 'public/index.html')
# source directory is static (path = "../static")
# destination directory is public (path="../public")

# step one is delete all contents of the destination directory
# function will be recursive, so the base case is probably if it's a file,



main()