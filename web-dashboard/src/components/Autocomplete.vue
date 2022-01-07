<template>
    <div v-if="customers.length">
        <ul class="autocomplete">
            <li v-for="customer_id in customers" :key="customer_id" @click="onSelectUser(customer_id)">{{ customer_id }}</li>
        </ul>
    </div>
</template>

<script>
export default {
    name: 'Autocomplete',
    props: ["customers"],
    methods: {
        onSelectUser(userId) {
            // Prevent redundant navigation
            if (this.$route.params.id != userId) {
                this.$router.push({ name: 'User', params: { id: userId } });
            }
            this.$emit('closeAutocomplete');
        }
    }
}
</script>

<style scoped lang="scss">
.autocomplete {
    position: absolute;
    width: 100%;
    list-style: none;
    background-color: #fff;
    border-radius: 0 0 0.3rem 0.3rem;
    box-shadow: 0 0.75rem 1.875rem 0 rgb(90 97 105 / 5%);
    border-top: 1px solid #f7f7f7;
    padding: 1rem;
    cursor: pointer;

    li {
        padding: 1rem;
        border-radius: 0.6rem;
        &:not(:last-child) {
            margin-bottom: 1rem;
        }

        &:hover {
            background-color: #f7f7f7;
        }
    }
}
</style>