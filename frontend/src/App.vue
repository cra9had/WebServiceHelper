<template>
  <div id="app">
    <header>
      <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="container-fluid">
          <a class="navbar-brand">
            <img src="https://getbootstrap.com/docs/5.1/assets/brand/bootstrap-logo.svg" alt="" width="30" height="24">
          </a>
          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <li class="nav-item">
                <a class="nav-link" href="#">Link</a>
              </li>

            </ul>
            <form class="d-flex">
              <div v-if="!user_data['is_signed_up']">
                <a v-on:click="push_login_page" class="auth-button">Sign In</a>
              </div>
              <div v-else>
                <div class="dropdown">
                  <img :src="user_data['avatar_url']" alt="image" class="profile-image">
                  <button class="btn btn-secondary dropdown-toggle username-btn" type="button" id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false">
                    {{ user_data["username"] }}
                  </button>
                  <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
                    <li><a class="dropdown-item" href="#">Мой профиль</a></li>
                    <li><a class="dropdown-item" href="#">Another action</a></li>
                    <!-- <li><a class="dropdown-item" href="#" v-on:click="logout">Выйти</a></li> -->
                  </ul>
                </div>
              </div>
            </form>
          </div>
        </div>
      </nav>
    </header>
    <router-view v-on:LoginAuth="on_auth($event)"/>
  </div>
</template>

<script>
export default {
  name: 'App',
  data(){
    return {
      user_data: {
        "is_signed_up": false
      }
    }
  },
  async mounted(){  
    await this.get_user_data()
  },
  methods: {
    push_login_page(){
      this.$router.push({
        "name": "LoginPage"
      })
    },
    
    async set_user_data(data, is_signed_up){
      this.user_data = data
      this.user_data.is_signed_up = is_signed_up;
    },

    async on_auth(){
      await this.get_user_data()
      this.$router.push(
        "user/" + this.user_data["username"]
      )
    },

    async get_user_data(){
      if (localStorage.token){
        this.token = localStorage.token
        this.response = await fetch("http://127.0.0.1:8000/api/profile", {
          method: 'GET',
          headers: {
            "Content-Type": "application/json",
            "Authorization": "Token " + this.token
          }})
        if (await this.response.status === 200){
          await this.set_user_data(await this.response.json(), true)
        }
        else if (await this.response.status === 401){
          localStorage.token = ""
        }
      }
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
.auth-button {
  box-shadow:inset 0px 1px 0px 0px #ffffff;
  background-color:#f9f9f9;
  border-radius:6px;
  border:1px solid #dcdcdc;
  display:inline-block;
  cursor:pointer;
  color:#666666;
  font-family:Arial;
  font-size:15px;
  font-weight:bold;
  padding:6px 24px;
  text-decoration:none;
  text-shadow:0px 1px 0px #ffffff;
  margin-right: 2rem;
}
.auth-button:hover {
  background-color:#e9e9e9;
}
.auth-button:active {
  position:relative;
  top:1px;
}
.profile-image {
  height: 40px;
  width: 40px;
  border-radius: 50%;
  margin-right: 0.7rem;
  border: 1px solid black;
}
.username-btn {
  margin-right: 2rem;
}
</style>
