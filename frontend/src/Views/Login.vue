<template>
  <div class="container-sm" style="margin-top: 4rem">
    <h2>Sign In</h2>
    <hr>
    <form @submit.prevent="login">
      <div class="mb-3">
        <label for="InputEmail" class="form-label">Email address</label>
        <input type="email" class="form-control" id="InputEmail" aria-describedby="emailHelp">
      </div>
      <div class="mb-3">
        <label for="InputPassword" class="form-label">Password</label>
        <input type="password" class="form-control" id="InputPassword">
      </div>
      <div style="margin-top: 2rem">
      <button type="submit" class="btn btn-primary">Sing In</button>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: "Login",
  methods: {
    async login(){
      if (typeof localStorage.token !== "undefined"){
        alert("You're already loggined in")
        return;
      }
      this.email = document.getElementById("InputEmail").value
      this.password = document.getElementById("InputPassword").value
      this.response = await fetch("http://127.0.0.1:8000/api/login", {
        method: 'POST',
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({"user": {
            "email": this.email,
            "password": this.password
          }
        })})
      if (await this.response.status === 200){
        this.response_json = await this.response.json()
        localStorage.token = this.response_json["token"]
        this.$emit("LoginAuth")
        // await this.$router.push({
        //   name: "HomePage"
        // })
      }
      else {
        console.log(this.response)
      }
    }
  }
}
</script>

<style scoped>

</style>