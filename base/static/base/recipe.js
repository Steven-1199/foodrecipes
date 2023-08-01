document.addEventListener("DOMContentLoaded", function () {
  recipe_new_collection_btn = document.querySelector(
    ".recipe_new_collection_btn"
  );

  document
    .getElementById("save_collection_item_btn")
    .addEventListener("click", function (event) {
      let collectionName = [];
      document.querySelectorAll("#collection_checkbox").forEach(function (i) {
        if (i.checked) {
          collectionName.push(i.value);
        }
      });

      if (collectionName.length > 0) {
        fetch(`/newCollectionItem`, {
          method: "POST",
          body: JSON.stringify({
            collectionName: collectionName,
            recipe_id: window.location.pathname.split("/")[2],
          }),
        })
          .then((respone) => respone.json)
          .then((result) => {
            console.log(result);
            window.location.href = window.location.href;
          });
      }
    });

  //load new collection form
  recipe_new_collection_btn.addEventListener("click", function () {
    document.querySelector(
      ".modal-body"
    ).innerHTML += `<form><label>Collection Name: </lable><input class="new_collection_name" type="text"/><button style="margin-left: 10px" type="submit" id="create_collection">Create</button></form>`;
    //Create new collection Name
    document
      .getElementById("create_collection")
      .addEventListener("click", function (event) {
        if (document.querySelector(".new_collection_name").value != "") {
          fetch(`/profile/loadCollection`, {
            method: "POST",
            body: JSON.stringify({
              collectionName: document.querySelector(".new_collection_name")
                .value,
            }),
          })
            .then((respone) => respone.json)
            .then((result) => {
              console.log(result);
              load_collection_name();
            });
          event.preventDefault();
        }
      });
  });
});

//Display Collections Name
function load_collection_name() {
  fetch(`/profile/loadCollection`)
    .then((respone) => respone.json())
    .then(function (items) {
      document.querySelector(".check_container").innerHTML = "";

      items["collectionName"].forEach(function (item) {
        document.querySelector(".check_container").innerHTML += `<div>
                <input type="checkbox" id="collection_checkbox" value="${item.id}"/>
                <label for="collection_checkbox">${item.collection_name}</label>
                
              </div>`;
      });
    });
}
