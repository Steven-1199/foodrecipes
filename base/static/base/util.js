let stringDirection = "";
const categories = {
  TOPIC: ["Quick and Easy", "30 Minutes Meals", "Comform Food"],
  MEALS: ["Lunch", "Breakfast", "Salad", "Side Dish", "Soup"],
  CUSINES: ["Thai", "Chinese", "Korean", "Japanese", "Italian", "French"],
};

document.addEventListener("DOMContentLoaded", function () {
  const ratingStars = [...document.getElementsByClassName("rating__star")];

  executeRating(ratingStars);

  category_view();
  if (window.location.pathname == "/shareRecipes") {
    document
      .querySelector(".select_categories")
      .addEventListener("click", function (event) {
        document.querySelector(".categories_views").value += `${
          document.querySelector(".select_category").value
        }, `;
        document.querySelector(".categories").value += `${
          document.querySelector(".select_category").value
        }, `;
        document.querySelector(".select_category").value = "";
        event.preventDefault();
      });

    document.querySelector("#step_done").addEventListener("click", step_done);

    document.querySelector(".addStep").addEventListener(
      "click",
      (() => {
        i = 2;
        let y = i - 1;
        function addStep(event) {
          if (document.querySelector(`#step${y.toString()}`).value != "") {
            stringDirection += `Step ${y}: ${
              document.querySelector(`#step${y.toString()}`).value
            }; `;
            document.querySelector(`#step${y.toString()}`).style.display =
              "none";
            document.querySelector(
              `#step${y.toString()}View`
            ).innerHTML += `<p>${
              document.querySelector(`#step${y.toString()}`).value
            }</p>`;
            document.querySelector(
              ".step_textarea_container"
            ).innerHTML += ` <div>
          
          <span>Step ${i}: </span>
          <textarea type="text" class="step" id="step${i}"></textarea>
          <div id="step${i}View"></div>
        </div>`;

            y = y + 1;
            i++;
          }

          event.preventDefault();
        }

        return addStep;
      })()
    );
    document
      .querySelector(".resetStep")
      .addEventListener("click", function (event) {
        document.querySelector(".step_finish").value = "";
        stringDirection = "";
        document.querySelector(".step_textarea_container").innerHTML = "";
        document.querySelector(".step_textarea_container").innerHTML += ` <div>
        
    <span>Step 1: </span>
    <textarea type="text" class="step" id="step1"></textarea>
    <div id="step1View"></div>
  </div>`;
        event.preventDefault();
      });
  }
});

function executeRating(stars) {
  const starClassActive = "rating__star fas fa-star";
  const starClassInactive = "rating__star far fa-star";
  const starsLength = stars.length;
  let i;
  let rating = -1;

  stars.map((star) => {
    star.onclick = () => {
      i = stars.indexOf(star);

      if (star.className === starClassInactive) {
        rating = -1;
        for (i; i >= 0; --i) {
          rating++;
          stars[i].className = starClassActive;
        }
      } else {
        rating = i - 1;
        for (i; i < starsLength; ++i) {
          stars[i].className = starClassInactive;
        }
      }
      document.querySelector(".ratingInput").value = rating;
    };
  });
}

function category_view() {
  document.querySelector(".category_inner_container").insertAdjacentHTML(
    "beforebegin",
    `<nav>
    <ul>
      <li><a href="/">ALL</a>
        
      </li>
    </ul>
  </nav>`
  );
  for (let categorie in categories) {
    document.querySelector(".category_inner_container").insertAdjacentHTML(
      "beforebegin",
      `<nav>
      <ul>
        <li><a href="#">${categorie}</a>
          <ul class="category_list_items_${categorie}">
            
          </ul>
        </li>
      </ul>
    </nav>`
    );

    categories[categorie].forEach(function (value) {
      if (window.location.pathname == "/shareRecipes") {
        document.querySelector(
          "#category_form"
        ).innerHTML += `<option value="${value}">${value}</option>`;
      }
      document.querySelector(
        `.category_list_items_${categorie}`
      ).innerHTML += `<li><a href="/?category=${value}">${value}</a></li>`;
    });
  }
}
function step_done(event) {
  document.querySelector(".step_finish").value = stringDirection;
  document.querySelectorAll(".step").forEach(function (value, index) {
    if (
      index == document.querySelectorAll(".step").length - 1 &&
      value.value != ""
    ) {
      document.querySelector(".step_finish").value += `Step ${index + 1}: ${
        value.value
      }; `;
    }
  });

  event.preventDefault();
}
