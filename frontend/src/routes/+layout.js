import { metadata } from '$lib/constants';

/** @type {import('./$types').LayoutLoad} */
export async function load() {
    return {
        title: metadata.name,
        data: [
            {
                layout: 'auth',
                linktree: [ 
                    { href: '/editor', label: 'Editor'},
                    { href: '/settings', label: 'Settings'}
                ]
            }
        ]
    };
}
