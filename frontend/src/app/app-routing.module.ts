import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {SongListComponent} from './song-list/song-list.component';
import {SongFormComponent} from './song-form/song-form.component';


const routes: Routes = [
  { path: '', redirectTo: 'song-list', pathMatch: 'full' },
  { path: 'song-list', component: SongListComponent },
  { path: 'song-form', component: SongFormComponent },
  {path: 'song-form/:id', component: SongFormComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
