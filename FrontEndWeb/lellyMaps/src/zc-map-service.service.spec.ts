import { TestBed } from '@angular/core/testing';

import { ZcMapServiceService } from './zc-map-service.service';

describe('ZcMapServiceService', () => {
  let service: ZcMapServiceService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ZcMapServiceService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
