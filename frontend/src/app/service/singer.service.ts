import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class SingerService {

  constructor(private http: HttpClient) { }

  getSingers() {
    return this.http.get <any[]>('/api/person/list');
  }

  getSinger(id: string) {
    return this.http.get('/api/person/list');
  }

  deleteSinger(id: string) {
    return this.http.delete('/api/person/' + id + '/delete');
  }

  createSinger(singers) {
    return this.http.post('/api/person/create', singers);
  }

  updateSinger(singers) {
    return this.http.put('/api/person/' + singers.id + '/update', singers);
  }
}
