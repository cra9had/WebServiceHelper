<template>
  <div class="container-sm" style="margin-top: 4rem">
    <h2 style="text-align: center">Sign Up</h2>
    <hr>
    <form @submit.prevent="register" style="margin-top: 2rem">
      <div class="mb-3">
        <label for="InputEmail" class="form-label">Email address</label>
        <input type="email" class="form-control" id="InputEmail" aria-describedby="emailHelp">
        <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
      </div>
      <div class="mb-3">
        <label for="InputUsername" class="form-label">Username</label>
        <input type="text" class="form-control" id="InputUsername">
      </div>
      <div class="mb-3">
        <label for="InputPassword" class="form-label">Password</label>
        <input type="password" class="form-control" id="InputPassword">
      </div>
      <button type="submit" class="btn btn-primary">Sing up</button>
      <a @click.prevent="go_login_page" style="margin-left: 2.5rem">I already have an account</a>
    </form>
  </div>
</template>

<script>
export default {
  name: "Register",
  async beforeMount(){
    if (await this.is_link_valid()){
      console.log("valid")
    } else {
      this.$router.push({
        "name": "PageNotFound",
        "params": {}
      })
    }

  },
  methods: {
    async register() {
      this.hash = this.$route.params.hash
      this.response = await fetch("http://127.0.0.1:8000/api/register", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
          "username": document.getElementById("InputUsername").value,
          "email": document.getElementById("InputEmail").value,
          "password": document.getElementById("InputPassword").value,
          "url_hash": this.hash
        })
      })
      this.response_json = await this.response.json()
      if (await this.response.status === 200){
        localStorage.token = this.response_json["token"]
        this.$emit("LoginAuth")
    
      }
      else{
      console.log(this.response_json)
    }},

    async is_link_valid() {
      if (localStorage.token) {
        alert("You're already loggined in")
        return false;
      }

      this.hash = this.$route.params.hash
      this.response = await fetch("http://127.0.0.1:8000/api/registerPage", {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            "url_hash": this.hash
          })
        })
      console.log(await this.response.status)
      return await this.response.status === 200;

    }
  }
}
</script>

<style scoped>

</style>