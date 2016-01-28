

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <gps.h>

#include "shm.h"

struct shmTime *shm_get() {
    int shmid;
    void *shm_time;

    // Try to create a new shared memory segment, in case gpsd has not started yet.
    shmid = shmget((key_t)(NTPD_SHM_KEY+unit), sizeof(struct shmTime), IPC_CREAT | IPC_EXCL | 0400);
    if (shmid < 0)
    {
        // Try to open an existing 
        shmid = shmget((key_t)(NTPD_SHM_KEY+unit), 0, 0600);
        if (shmid < 0) {
            return NULL;
        }
    }

    shm_time = (struct shmTime *)shmat(shmid, NULL, 0);
    if (shm_time == (void *)(-1)) {
        return NULL;
    }

    return shm_time;
}
