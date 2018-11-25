Vue.use(VeeValidate);

new Vue({
    el: '#app',
    $_veeValidate: {
        validator: 'new'
    },

    data: () => ({
        signupName: "",
        signupEmail: "",
        signupPassword: "",
        signinEmail: "",
        signinPassword: "",
        selectFeeder: null,
        show1: false,
        dictionary: {
            attributes: {
                email: 'E-mail Address'
                // custom attributes
            },
            custom: {
                name: {
                    required: () => 'Nombre no puede estar vacio',
                    max: "El nombre no puede ser mayor a 85 caracteres",
                    // custom messages
                }
            },
            selectFeeder: {
                required: 'Se requiere seleccionar una alimentadora'
            }
        }
    }),

    mounted () {
        this.$validator.localize('en', this.dictionary)
    },

    methods: {
        submit() {
            this.$validator.validateAll()
        },
        clear() {
            this.name = ""
            this.email = ""
            this.password = ""
            this.selectFeeder = null
            this.$validator.reset()
        }
    },

});


/*
{
        name: "",
        emmail: "",
        password: "",
        return {
            loading3: false,
            selectFeeder: 0,
            items: [],

        }
    }
});
*/

