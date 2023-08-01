if (window.location.href.indexOf("savedcollection") != -1) {
  let saved_collection_btn = document.getElementById("saved_collection_btn");

  document.getElementById(
    "profile_header_right_saved_collection"
  ).style.display = "block";
  document.getElementById("profile_header_right_home").style.display = "none";
  saved_collection_btn.style.borderLeft = "5px #71c6dd solid";
  saved_collection_btn.style.color = "#71c6dd";
  saved_collection_btn.style.fontWeight = "bold";

  profile_load_collection_name();
} else if (window.location.href.indexOf("collection") != -1) {
  let collectionName = window.location.search.split("=")[1].replace(";", " ");
  document.getElementById(
    "profile_header_right_saved_collection"
  ).style.display = "block";
  document.getElementById("profile_header_right_home").style.display = "none";

  profile_load_collection_item(collectionName);
} else if (window.location.href.indexOf("following") != -1) {
  let following_btn = document.getElementById("following_btn");
  document.getElementById("profile_header_right_home").style.display = "none";
  following_btn.style.borderLeft = "5px #71c6dd solid";
  following_btn.style.color = "#71c6dd";
  following_btn.style.fontWeight = "bold";

  document.querySelector(".profile_header_right_following").style.display =
    "block";
} else {
  let home_btn = document.getElementById("home_btn");
  home_btn.style.borderLeft = "5px #71c6dd solid";
  home_btn.style.color = "#71c6dd";
  home_btn.style.fontWeight = "bold";
}

function profile_load_collection_item(collectionName) {
  fetch(`/profile/loadCollectionItem/${collectionName}`)
    .then((respone) => respone.json())
    .then(function (items) {
      document.querySelector(
        ".header_collection"
      ).innerHTML = `${collectionName}`;
      document.querySelector(
        ".profile_header_right_saved_collection_card_container"
      ).innerHTML = "";
      items["collectionItems"].forEach(function (item, index) {
        document.querySelector(
          ".profile_header_right_saved_collection_card_container"
        ).innerHTML += ` <a href="/recipe/${item["recipe_id"]}" style="text-decoration: none; color:black" onMouseOver="this.style.opacity='0.8';this.style.cursor='pointer'"
        onMouseOut="this.style.opacity='1'">
        <div  class="card mb-3" style="width: 300px; min-height: 300px">
        <div  style=" height: 200px;background-color: rgb(206, 203, 203); display: flex; justify-content: center; align-items: center; overflow:hidden" class="card-img collection_card_innercontainer">
          <img src="${item["recipe_img"]}" style="width: 100%"/>      
        </div>
        <div class="card-body">
          <h5 class="card-title">${item["recipe_title"]}</h5>
          <div class="recipe_post_divider">
      <div>
        <span class="badge text-bg-light">RATING: </span
        ><span class="badge text-bg-light"
          >${item["recipe_rating"]["avg_rating"]}
          <i class="rating__star fas fa-star" style="color: #dabd18b2"></i
        ></span>
      </div>
      <div style="padding-left: 10px">
        <span class="badge text-bg-light"
          >${item["recipe_review"]["count_review"]} REVIEWS</span
        >
      </div>
     
    </div>
    </a>    
        </div>
        <button onclick="removeCollectionItem(${item.id})" style="width:fit-content; margin: 0 0px 10px 10px" type="button" class="btn btn-light"><svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" fill="currentColor" class="bi bi-dash-circle" viewBox="0 0 16 16">
        <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/>
        <path d="M4 8a.5.5 0 0 1 .5-.5h7a.5.5 0 0 1 0 1h-7A.5.5 0 0 1 4 8z"/>
      </svg> Remove</button>
      </div>
        `;
      });
    });
}
function removeCollectionItem(collectionItemId) {
  fetch(`/deleteCollectionItem/${collectionItemId}`, { method: "delete" })
    .then((response) => response.json)
    .then(function (result) {
      window.location.href = window.location.href;
    });
}
function profile_load_collection_name() {
  fetch(`/profile/loadCollection`)
    .then((respone) => respone.json())
    .then(function (items) {
      document.querySelector(
        ".profile_header_right_saved_collection_card_container"
      ).innerHTML = "";

      items["collectionName"].forEach(function (item, index) {
        document.querySelector(
          ".profile_header_right_saved_collection_card_container"
        ).innerHTML += ` <a onMouseOver="this.style.opacity='0.8';this.style.cursor='pointer'"
        onMouseOut="this.style.opacity='1'" href="?collection=${item.collection_name.replace(
          " ",
          ";"
        )}" style="text-decoration: none; color:black">
        <div  class="card mb-3" style="width: 200px">
        <div  style="overflow:hidden ;height: 200px;background-color: rgb(206, 203, 203); display: flex; justify-content: center; align-items: center;" class="card-img collection_card_innercontainer">
        ${
          items["a"][index] && item.collection_name != "Saved Item"
            ? `<img src="${items["a"][index]}" style="width: 200px"/>`
            : ""
        }
          <svg xmlns="http://www.w3.org/2000/svg" width="70" height="70" fill="#71c6dd" class="bi bi-bookmark-heart-fill" viewBox="0 0 16 16">
            <path d="M2 15.5a.5.5 0 0 0 .74.439L8 13.069l5.26 2.87A.5.5 0 0 0 14 15.5V2a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2v13.5zM8 4.41c1.387-1.425 4.854 1.07 0 4.277C3.146 5.48 6.613 2.986 8 4.412z"/>
          </svg>
        </div>
        <div class="card-body" style="padding-bottom: 5px">
          <h5 class="card-title">${item.collection_name}</h5>
          <span style="margin:0">${
            items["collectionItemCount"][index]["count_item"]
          } items</span>
          </div>
          </a>
         ${
           item.collection_name != "Saved Item"
             ? ` <button onclick="profileRemoveCollectionItem(${item.id})" style="width:fit-content; margin: 0 0px 10px 10px" type="button" class="btn btn-light"><svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" fill="currentColor" class="bi bi-dash-circle" viewBox="0 0 16 16">
        <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/>
        <path d="M4 8a.5.5 0 0 1 .5-.5h7a.5.5 0 0 1 0 1h-7A.5.5 0 0 1 4 8z"/>
      </svg> Remove</button>`
             : ""
         }

        </div>
        
        </div>

      </div>
        `;
      });
      document.querySelector(
        ".profile_header_right_saved_collection_card_container"
      ).innerHTML += ` <div href="" style="text-decoration: none; color:black"  data-bs-toggle="modal" data-bs-target="#staticBackdrop">
      <div onMouseOver="this.style.opacity='0.8';this.style.cursor='pointer'"
      onMouseOut="this.style.opacity='1'" class="card mb-3" style="width: 200px; height:290px">
      <div  style=" height: 200px;background-color: rgb(206, 203, 203); display: flex; justify-content: center; align-items: center;" class="card-img collection_card_innercontainer">
    
      <svg xmlns="http://www.w3.org/2000/svg" width="70" height="70" fill="currentColor" class="bi bi-plus-square" viewBox="0 0 16 16">
      <path d="M14 1a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h12zM2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2z"/>
      <path d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4z"/>
    </svg>
      </div>
      <div class="card-body">
        <h5 class="card-title">Create Collection</h5>
        
      </div>
    </div>
      </div>`;
      document.querySelector(
        ".profile_header_right_saved_collection_card_container"
      ).innerHTML += `<div class="modal fade" id="staticBackdrop" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="staticBackdropLabel">New Collection Title</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <input type="text" class="profile_new_collection">
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            <button type="button" class="btn btn-primary profile_create_new_collection">Create</button>
          </div>
        </div>
      </div>
    </div>`;
      document.querySelector(".profile_create_new_collection"),
        addEventListener("click", function (e) {
          let v = document.querySelector(".profile_new_collection").value;
          if (v != "") {
            fetch(`/profile/loadCollection`, {
              method: "POST",
              body: JSON.stringify({
                collectionName: v,
              }),
            })
              .then((respone) => respone.json)
              .then((result) => {
                console.log(result);
              });
            window.location.href = window.location.href;
            e.preventDefault();
          }
        });
    });
}
function profileRemoveCollectionItem(id) {
  fetch(`/deleteCollection/${id}`, { method: "delete" })
    .then((response) => response.json)
    .then(function (result) {
      window.location.href = window.location.href;
    });
}
