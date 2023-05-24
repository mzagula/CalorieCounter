function showRecipe(recipeId) {
    window.location.href = `/recip_estima/recipe_detail/${recipeId}`;
}
function showConfirmationDialog(recipeId) {
    document.getElementById("confirmation-dialog").style.display = "block";
}
function hideConfirmationDialog() {
    document.getElementById("confirmation-dialog").style.display = "none";
}
function deleteRecipe(recipeId) {
    window.location.href = `/recip_estima/recipe_delete/${recipeId}`;
}