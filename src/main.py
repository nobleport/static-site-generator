from file_generation import static_to_public, generate_page, generate_pages_recursive

def main():
    static_to_public("./static", './public')
    # generate_page('content/index.md', 'template.html', 'public/index.html')
    generate_pages_recursive('./content', 'template.html', './public')
# source directory is static (path = "../static")
# destination directory is public (path="../public")

# step one is delete all contents of the destination directory
# function will be recursive, so the base case is probably if it's a file,



main()