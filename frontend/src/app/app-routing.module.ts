import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {SongListComponent} from './song-list/song-list.component';
import {SongFormComponent} from './song-form/song-form.component';
import {SingerListComponent} from './singer-list/singer-list.component';
import {SingerFormComponent} from './singer-form/singer-form.component';


const routes: Routes = [
  { path: '', redirectTo: 'song-list', pathMatch: 'full' },
  { path: 'song-list', component: SongListComponent },
  { path: 'song-form', component: SongFormComponent },
  {path: 'song-form/:id', component: SongFormComponent},
  { path: 'singer-list', component: SingerListComponent },
  { path: 'singer-form', component: SingerFormComponent },
  {path: 'singer-form/:id', component: SingerFormComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
