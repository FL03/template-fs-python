<script>
	/** @type {import('./$types').LayoutData} */
	export let data;
	import '$lib/assets/css/styles.css';
	import { Navbar, Sidebar, Toolbar, WalletToggle } from '$lib';

	let open = false;

	
</script>

<div class="bg-gradient-to-br from-zinc-900 via-zinc-800 to-zinc-900 flex flex-col items-center justify-center m-0 p-0 z-0 min-h-screen min-w-full max-w-screen">
	<Navbar name={data.title}>
		<WalletToggle/>
	</Navbar>
	<div class="flex flex-col grow items-center justify-center min-h-full max-h-screen min-w-full max-w-screen z-0">
		<main class="container mx-auto">
			<slot/>
		</main>
	</div>
	
	<Toolbar 
		linktree={data.data[0].linktree} 
		bind:sidebar={open}
	/>
</div>

<Sidebar bind:open>
	Sidebar
</Sidebar>


<style>
	
</style>
