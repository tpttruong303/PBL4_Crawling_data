<script setup lang="ts">
import { ref} from "vue"
import { useRouter } from "vue-router"
import { useAuthStore } from "../stores/auth"

defineProps<{}>()
const router = useRouter()
const authStore = useAuthStore()
const isLogin = ref<boolean | undefined>(false)

const goToLogin: () => void = () => {
    router.push("/login")
}
const goToRegister: () => void = () => {
    router.push("/register")
}
const goToMainJob: () => void = () => {
    router.push("/mainjob")
}
const goToUser: () => void = () => {
    router.push("/user")
}
const goToAdmin: () => void = () => {
    router.push("/admin")
}

const logout: () => Promise<void> = async () => {
    try {
        localStorage.removeItem("access_token")
        localStorage.removeItem("refresh_token")
        authStore.setAuthStore({
            user: {
                email: "",
                password: "",
            },
            isLoggedIn: false,
            isAdmin: false,
        })
        router.push("/login")
    } catch (error) {
        console.error(error)
    }
}
isLogin.value = authStore.getIsLoggedIn()
</script>

<template>
    <div class="nav-container">
        <div class="nav-container__body">
            <button @click="goToMainJob" class="nav-container__body__logo">PBL4: Web tìm kiếm việc làm</button>
            <div class="nav-container__body__action" v-if="!authStore.getIsLoggedIn()">
                <button  @click="goToLogin" class="nav-container__body__btn">Đăng nhập</button>
                <button  @click="goToRegister" plain class="nav-container__body__btn">Đăng ký</button>
            </div>
            <div class="nav-container__body__info" v-else>
                <div class="avatar-flex">
                    <img :src="authStore.getAvatar()" alt="">
                <p>{{ authStore.getUserName() }}</p>
                </div>
                    <div class="dropdown">
                        <button class="dropbtn">Menu <el-icon><CaretBottom /></el-icon></button>
                            <div class="dropdown-content">
                                <a v-if="useAuthStore().getIsAdmin()" @click="goToAdmin()">Quản lý tài khoản</a>
                                <a @click="goToUser()">Thông tin cá nhân</a>
                                <a @click="logout()" >Đăng xuất</a>
                            </div>
                    </div>
            </div>  
        </div>
    </div>
</template>

<style lang="scss" scoped>
.nav-container {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 70px;
    display: flex;
    justify-content: center;
    border-bottom: 1px solid #ebeef5;
    background-color: #fff;
    box-shadow: 0 1px 20px rgba(44, 127, 217, 0.5);

    &__body {
        width: 1200px;
        max-width: 100%;
        padding: 0 20px;
        display: flex;
        justify-content: space-between;
        align-items: center;

        &__logo {
            font-size: 1.5rem;
            font-weight: 700;
            color: #77bbe8;
            background-color: white;
            border: 1px solid white;
            cursor: pointer;
        }

        &__action {
            display: flex;
            width: 320px;
        }
        &__info {
            display: flex;
            align-items: center;
            gap: 10px;
            &__icon-right {
                cursor: pointer;
                &:hover {
                    transform: translateX(10px);
                    transition: all 0.2s linear;
                }
            }
        }
        &__btn {
            border-radius: 25px;
            width: 80%;
            height: 40px;
            font-size: 0.8rem;
            color: white;
            font-weight: 700;
            background: #0069db;
            border: 0px;
            cursor: pointer;
            transition: opacity 0.25s ease-out;
            margin: 0 5px;
            &:hover{
                color: #0069db;
                background-color: #fff;
                border: 1px solid #0069db;
                transition: all 0.3s ease-in-out;
            }
        }
    }
}
.nav-container__body__info img {
    width: 30px;
    height: 30px;
    border-radius: 50%;
}
.nav-container__body__info p {
    font-size: 12px;
    color: white;
}
.avatar-flex {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 8px;
    padding: 12px 20px;
    background-color: #0069db;
    border-radius: 25px;
}
.dropbtn {
  background-color: #0069db;
  color: white;
  padding: 18px 38px;
  border: none;
  cursor: pointer;
  font-size: 12px;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 4px;
  border-radius: 25px;
}
.dropbtn:hover {
    color: #0069db;
    background-color: #fff;
    border: 1px solid #0069db;
    transition: all 0.3s ease-in-out;
}

.dropdown {
  position: relative;
  display: inline-block;
  font-size: 12px;
}

.dropdown-content {
  display: none;
  position: absolute;
  background-color: #f9f9f9;
  top: 95%;
  min-width: 100px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
  cursor: pointer;
}

.dropdown-content a {
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
}

.dropdown-content a:hover {
  background-color: #f1f1f1;
}

.dropdown:hover .dropdown-content {
  display: block;
  width: 150px;
}
</style>
