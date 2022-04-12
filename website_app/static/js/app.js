const deletePost = (event, postID, categoryID, subcategoryID) => {
  axios.post(`/delete-post/${postID}/`)
    .then(() => {
      window.location.href = `/categories/${categoryID}/subcategory/${subcategoryID}/`
    })
    .catch((error) => {
      console.log(error)
      window.location.href = '/error/couldnt_delete'
    })
}

const deleteCategory = (event, categoryID) => {
  axios.post(`/delete-category/${categoryID}/`)
    .then((response) => {
      window.location.href = '/categories/'
    })
    .catch((error) => {
      console.log(error)
      window.location.href = '/error/couldnt_delete'
    })
}
const deleteSubcategory = (event, categoryID, subcategoryID) => {
  axios.post(`/delete-subcategory/${subcategoryID}/`)
    .then((response) => {
      window.location.href = `/categories/${categoryID}/`
    })
    .catch((error) => {
      console.log(error)
      window.location.href = '/error/couldnt_delete'
    })
}

