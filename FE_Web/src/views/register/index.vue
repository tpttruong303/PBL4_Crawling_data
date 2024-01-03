<script setup lang="ts">
import { useRouter } from "vue-router"
import { ref} from "vue"
import { ISignUp } from "@/types/user"
import { registerApi } from "@/services/user.service"
import { ElNotification } from "element-plus"

const router = useRouter()

const user = ref<ISignUp>({
    email: "",
    name: "",
    password: "",
    avatar: "",
    age: 0
})
const isEnterValue = ref<boolean[]>([false])
const isMatchPassword = ref<boolean>(false)
const rePassword = ref<string>("")

const signUp = async () => {
    try {
        if (!checkInput()) {
            console.log("hihii")

            return
        }
        if (rePassword.value != user.value.password) {
            isMatchPassword.value = true
            return
        }
        isMatchPassword.value = false
        await registerApi(user.value)
        ElNotification({
            title: "Thành công",
            message: "Tạo tại khoản thành công!",
            type: "success",
        })
        router.push("/login")
    } catch (error) {
        ElNotification({
            title: "Thất bại", 
            message: "Tạo tại khoản thất bại, vui lòng kiểm tra lại!",
            type: "error",
        })
        console.error(error)
    }
}

const checkInput: () => boolean = () => {
    isEnterValue.value[0] = !user.value.email
    isEnterValue.value[1] = !user.value.name
    isEnterValue.value[2] = !user.value.password
    isEnterValue.value[3] = !rePassword.value
    return !isEnterValue.value.some((value) => value === true)
}
</script>

<template>
    <div class="row">
        <div class="grid__column-4 banner-container">
            <div class="banner-container__circle"></div>
            <div class="banner-container__content">
                <h1>Xây dựng
                    <br>
                <b>Sự nghiệp
                    <br>
                <span class="text-warning">thành công!</span>
                </b>
                </h1>
            </div>
        </div>
        <div class="grid__column-6">
            <div class="login-container">
                <div class="login-container__form">
                    <h1 class="login-container__form__title">Đăng ký</h1>
                    <div class="login-container__form__content">
                    <div>
                        <el-input v-model="user.email" validate-event type="email" placeholder="Nhập Email" class="login-container__form__content__input" />
                        <span class="login-container__form__content__error" v-show="isEnterValue[0]">Vui lòng nhập emal</span>
                    </div>
                    <div>
                        <el-input v-model="user.name" placeholder="Nhập tên của bạn" class="login-container__form__content__input" />
                        <span class="login-container__form__content__error" v-show="isEnterValue[1]">Vui lòng nhập họ tên</span>
                    </div>
                    <div>
                        <el-input v-model="user.password" type="password" placeholder="Nhập mật khẩu" show-password class="login-container__form__content__input" />
                        <span class="login-container__form__content__error" v-show="isEnterValue[2]">Vui lòng nhập mật khẩu</span>
                    </div>
                    <div>
                        <el-input v-model="rePassword" type="password" placeholder="Xác nhận mật khẩu" show-password class="login-container__form__content__input" />
                        <span class="login-container__form__content__error" v-show="isEnterValue[3]">Vui lòng nhập để xác nhận mật khẩu</span>
                    </div>
                    <span class="login-container__form__content__error" v-show="isMatchPassword">Mật khẩu cảu bạn không chính xác. Vui lòng nhập lại!</span>
                    <el-button @click="signUp" class="login-container__form__content__submit" type="primary">Đăng ký</el-button>
                    <div class="login-container__form__content__login">
                        <span>Bạn đã có tài khoản?</span>
                        <el-link type="primary" href="/login">Đăng nhập</el-link>
                  </div>
            </div>
        </div>
        </div>
        </div>
    </div>
    
</template>

<style lang="scss" scoped>
.row {
    display: flex;
    flex-wrap: wrap;
    margin-right: -15px;
    margin-left: -15px;
}
.grid__column-4{
    padding-left: 5px;
    padding-right: 5px;
    width: 40%;
}
.grid__column-6{
    padding-left: 5px;
    padding-right: 5px;
    width: 60%;
    background-color: #ffffff;
}
.banner-container{
    background-image: linear-gradient(to bottom, #0071FF, #0130CB);
    position: relative;
    overflow: hidden;
    color: #fff !important;
    align-items: center !important;
    justify-content: center !important;
    height: 646px;
}
.banner-container__circle{
    height: 40vw;
    width: 40vw;
    border-radius: 50%;
    background-color: rgba(255,255,255,0.08);
    position: absolute;
    top: -15vw;
    left: -15vw;
}
.banner-container__content h1{
    position: absolute;
    top: 20%;
    left: calc(50% - 150px);
    width: 300px;
    font-size: 32px;
    line-height: 1.2;
    color: #fff !important;
}
.banner-container__content b{
    font-size: 54px;
    font-weight: bolder;
}
.text-warning{
    color: #f7b500 ;
    font-size: 48px;
}
.login-container {
    width: 100%;
    height: 100%;
    overflow: hidden;
    &__form {
        width: 50%;
        margin: auto;
        margin-top: 100px;
        background: #fff;
        padding: 40px 20px 60px;
        box-shadow: 0px 10px 50px 0px rgba(139, 139, 139, 0.4);;
        border-radius: 12px;
        &__title {
            font-weight: 700;
            font-size: 1.5rem;
            line-height: 2rem;
            margin-bottom: 2rem;
            text-align: center;
        }
        &__content {
            padding: 0 30px;
            display: flex;
            flex-direction: column;
            gap: 20px;
            &__co {
                display: flex;
                justify-content: space-between;
                align-items: center;
                width: 100%;
            }
            &__input,
            &__submit {
                width: 100%;
            }
            &__login {
                span {
                    font-size: 12px;
                    padding-right: 8px;
                }
            }
            &__error {
                font-size: 12px;
                color: red;
            }
        }
    }
}
</style>
