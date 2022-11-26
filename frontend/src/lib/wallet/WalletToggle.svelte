<script>
    import { connected, defaultEvmStores } from 'svelte-web3';

    export let bg = 'bg-gradient-to-r from-cyan-700 via-cyan-500 to-cyan-900';
    export let color = 'text-white';

	async function handle_click() {
		if ($connected) {
			defaultEvmStores.disconnect();
		} else {
			defaultEvmStores.setProvider();
		}
	}
</script>

	

<button 
    class="overflow-x-hidden py-1 px-2 inline-block mx-auto px-3 py-1 rounded items-center justify-center {bg} {color} w-24" 
    on:click={handle_click}
>
    {#if $connected}
        Logout
    {:else}
        Login
    {/if}
</button>