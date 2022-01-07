<template>
  <div class="last-order">
    <h2>Dernière commande - Ticket #{{ lastOrder[0]['TICKET_ID'] }}</h2>
    <div class="flex-table">
        <div class="row flex-row header">
            <div class="flex-cell col-4">Libellé</div>
            <div class="flex-cell col-2">Maille</div>
            <div class="flex-cell col-2">Famille</div>
            <div class="flex-cell col-3">Univers</div>
            <div class="flex-cell col-1 price">Prix</div>
        </div>
        <div class="row flex-row" v-for="row, index in lastOrder" :key="index">
            <div class="flex-cell col-4">{{ row['LIBELLE'] }}</div>
            <div class="flex-cell col-2">{{ row['MAILLE'] }}</div>
            <div class="flex-cell col-2">{{ row['FAMILLE'] }}</div>
            <div class="flex-cell col-3">{{ row['UNIVERS'] }}</div>
            <div class="flex-cell col-1 price">{{ row['PRIX_NET'] }} €</div>
        </div>
    </div>
    <div class="total">
        <div class="row">
            <div class="col-6">
                <label>Quantité totale</label>
            </div>
            <div class="col-6">
                <span>{{ quantity }}</span>
            </div>
        </div>
        <div class="row">
            <div class="col-6">
                <label>Prix total</label>
            </div>
            <div class="col-6">
                <span>{{ total }} €</span>
            </div>
        </div>
    </div>
  </div>
</template>

<script>
export default {
    name: 'LastOrder',
    props: ['lastOrder'],
    data: () => ({
        quantity: 0,
        total: 0
    }),
    mounted: function () {
        this.quantity = this.lastOrder.length;
        this.total = this.lastOrder.reduce(function (previousValue, currentValue) {
            return previousValue + currentValue['PRIX_NET'];
        }, this.total).toFixed(2);
    }
}
</script>

<style scoped lang="scss">
.last-order {
    .flex-table {
        display: flex;
        flex-direction: column;
        border: 0;
        border-radius: 0.3rem;
        background-color: #fff;
        box-shadow: 0 0.75rem 1.875rem 0 rgb(90 97 105 / 5%) !important;
        padding: 1rem;
        margin: 2rem 0;

        .header {
            font-weight: bolder;
        }

        .flex-row {
            width: 100%;
            margin: auto;
            padding: 0.8rem 0;

            &:not(:last-child) {
                border-bottom: 1px solid #e2e2e2;
            }

            .flex-cell {
                margin: 0;
                padding: 0 1rem;
            }
        }
    }

    .total {
        max-width: 400px;
        padding-left: 2rem;

        label {
            font-weight: bolder;
            margin-bottom: 1rem;
        }
    }
}
</style>
