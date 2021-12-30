<template>
    <div class="search">
        <div class="input-group">
            <div class="input-group-prepend">
                <span class="input-group-text" id="search-addon">
                    <b-icon-search></b-icon-search>
                </span>
            </div>
            <input type="text" class="form-control find-user" id="find-user" placeholder="Find an user by id..." v-model="search">
        </div>
        <Autocomplete v-if="search" v-click-outside="closeAutocomplete" @closeAutocomplete="closeAutocomplete"/>
    </div>
</template>

<script>
import Autocomplete from './Autocomplete.vue'

export default {
    name: 'Search',
    components: {
        Autocomplete
    },
    data: () => ({
        search: ""
    }),
    methods: {
        closeAutocomplete() {
            this.search = "";
        }
    }
}
</script>

<style scoped lang="scss">
.search {
    position: relative;
    margin: 1rem 0 5rem 0;

    .input-group {
        box-shadow: 0 0.75rem 1.875rem 0 rgb(90 97 105 / 5%);

        .input-group-prepend {
            display: flex;
            flex-direction: column;
            justify-content: center;
            background-color: #fff;
        }

        #search-addon {
            padding-left: 2rem;
            background-color: #fff;
            border: 0;
            color: #3d5170;
        }

        input {
            border: 0;
            border-radius: 0.3rem;
            padding: 1rem 2rem;
            &:focus {
                outline:0px !important;
                -webkit-appearance:none;
                box-shadow: none !important;
            }
        }
    }
}
</style>
