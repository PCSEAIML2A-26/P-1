document.addEventListener("DOMContentLoaded", function () {
    
    const blogs = [
        {
            category: "JS",
            title: "Introduction to JavaScript",
            content: "JavaScript is a programming language that enables interactive web pages.",
        },
        {
            category: "HTML",
            title: "HTML Basics",
            content: "HTML (HyperText Markup Language) is the standard markup language for creating web pages.",
        },
        {
            category: "CSS",
            title: "Styling with CSS",
            content: "CSS (Cascading Style Sheets) is used for styling web pages and making them visually appealing.",
        },
        {
            category: "ML",
            title: "Introduction to Machine Learning",
            content: "Machine Learning is a field of artificial intelligence that focuses on building systems that can learn from and make decisions based on data.",
        },
    ];

   
    function createBlogElement(blog) {
        const blogElement = document.createElement("div");
        blogElement.classList.add("blog");

        const categoryElement = document.createElement("h2");
        categoryElement.textContent = blog.category;

        const titleElement = document.createElement("h3");
        titleElement.textContent = blog.title;

        const contentElement = document.createElement("p");
        contentElement.textContent = blog.content;

        blogElement.appendChild(categoryElement);
        blogElement.appendChild(titleElement);
        blogElement.appendChild(contentElement);

        return blogElement;
    }

    
    function addBlogsToPage() {
        const blogContainer = document.getElementById("blog-container");

        blogs.forEach(blog => {
            const blogElement = createBlogElement(blog);
            blogContainer.appendChild(blogElement);
        });
    }

    
    addBlogsToPage();
});