// THEME COLOR
const colorScheme = window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
const setTheme = (theme) => {
    document.documentElement.setAttribute("data-theme", theme);
    localStorage.setItem("theme", theme);
}

setTheme(localStorage.getItem("theme") || colorScheme);

// SWITCH THEME
const toggleSwitch = document.querySelector('#theme-toggle');

toggleSwitch.addEventListener('change', function() {

    if (this.checked) {
        document.documentElement.setAttribute('data-theme', 'dark');
        localStorage.setItem('theme', 'dark');
    }
    else
    {
        document.documentElement.setAttribute('data-theme', 'light');
        localStorage.setItem('theme', 'light');
    }
});

const currentTheme = localStorage.getItem('theme');
const textTheme = document.querySelector(".theme");

if (currentTheme) {
    document.documentElement.setAttribute('data-theme', currentTheme);

    if (currentTheme === 'dark') {
        toggleSwitch.checked = true;
    }
}

// SEARCH OBJECTS
const search = document.getElementById("search");

search.addEventListener('keyup', (e) => {
    if (e.target.matches("#search")) {

        if (e.key === "Escape" || e.key === "Delete") e.target.value = "";

        if (document.title === "Home") {
            document.querySelectorAll(".director_name").forEach(director => {
                let cardDirector = director.closest(".directors")

                director.textContent.toLowerCase().includes(e.target.value.toLowerCase())
                    ?cardDirector.classList.remove("filter")
                    :cardDirector.classList.add("filter");
            })

            document.querySelectorAll(".actor_name").forEach(actor => {
                let cardActor = actor.closest(".actors")

                actor.textContent.toLowerCase().includes(e.target.value.toLowerCase())
                    ?cardActor.classList.remove("filter")
                    :cardActor.classList.add("filter");
            })
        }
        else
        {
            document.querySelectorAll(".movie_title").forEach(movie => {
                let cardMovie = movie.closest(".movies")

                movie.textContent.toLowerCase().includes(e.target.value.toLowerCase())
                    ?cardMovie.classList.remove("filter")
                    :cardMovie.classList.add("filter");
            })
        }
    }
})

// GET THE SUMMARY
const movies = document.querySelectorAll(".movies");

const descriptionMovie = document.getElementById("description_movie");
const descriptionSummary = document.getElementById("description_summary");
const summaryAside = document.getElementById("movie_summary_aside");
const summary = document.getElementById("movie_summary");

const defaultDescription = document.getElementById("default-description");

movies.forEach(movie => {
    movie.addEventListener('click', () => {
        const movieTitle = movie.dataset.title;
        summaryAside.textContent = movieTitle;

        const movieSummary = movie.dataset.summary;
        summary.textContent = movieSummary;

        if (summary.textContent == movieSummary) {
            defaultDescription.style.display = "none";

            descriptionSummary.style.display = "flex";
            summary.style.display = "inline-block";

            let descriptionHeight = descriptionSummary.offsetHeight;
            console.log(descriptionHeight);

            descriptionMovie.style.display = "flex";
            descriptionMovie.style.height = descriptionHeight + "px";
            summaryAside.style.display = "inline-block";
        }
    })
})

