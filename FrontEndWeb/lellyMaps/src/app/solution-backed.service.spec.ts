import { TestBed } from '@angular/core/testing';

import { SolutionBackedService } from './solution-backed.service';

describe('SolutionBackedService', () => {
  let service: SolutionBackedService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(SolutionBackedService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
