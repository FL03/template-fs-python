<script>
	/** @type {import('./$types').LayoutData} */
	export let data;
	import '$lib/styles.css';
	import { Navbar, Sidebar, Toolbar } from '$lib';

	import { connected, defaultEvmStores } from 'svelte-web3';

	let open = false;

	async function handle_click() {
		if ($connected) {
			defaultEvmStores.disconnect();
		} else {
			defaultEvmStores.setProvider();
		}
	}
</script>

	
<div class="bg-gradient-to-br from-zinc-900 via-zinc-800 to-zinc-900 flex flex-col items-center justify-center m-0 p-0 z-0 min-h-screen min-w-full max-w-screen">
	<Navbar name={data.title}>
		<button 
			class="overflow-x-hidden py-1 px-2 inline-block mx-auto px-3 py-1 rounded items-center justify-center bg-gradient-to-r from-cyan-700 via-cyan-500 to-cyan-900 text-white w-24" 
			on:click={handle_click}
		>
			{#if $connected}
				Logout
			{:else}
				Login
			{/if}
		</button>
	</Navbar>
	<main class="container mx-auto flex flex-col grow items-center justify-center min-h-full max-h-screen min-w-full max-w-screen z-0">
		<slot/>
	</main>
	<Toolbar linktree={[]} bind:sidebar={open}/>
</div>

<Sidebar bind:open>
	Sidebar
</Sidebar>




<style>
	
</style>
