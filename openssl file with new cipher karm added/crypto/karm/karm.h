/* crypto/karm/karm.h */
/* ====================================================================
 * Copyright (c) 2006 The OpenSSL Project.  All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 *
 * 1. Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 *
 * 2. Redistributions in binary form must reproduce the above copyright
 *    notice, this list of conditions and the following disclaimer in
 *    the documentation and/or other materials provided with the
 *    distribution.
 *
 * 3. All advertising materials mentioning features or use of this
 *    software must display the following acknowledgment:
 *    "This product includes software developed by the OpenSSL Project
 *    for use in the OpenSSL Toolkit. (http://www.openssl.org/)"
 *
 * 4. The names "OpenSSL Toolkit" and "OpenSSL Project" must not be used to
 *    endorse or promote products derived from this software without
 *    prior written permission. For written permission, please contact
 *    openssl-core@openssl.org.
 *
 * 5. Products derived from this software may not be called "OpenSSL"
 *    nor may "OpenSSL" appear in their names without prior written
 *    permission of the OpenSSL Project.
 *
 * 6. Redistributions of any form whatsoever must retain the following
 *    acknowledgment:
 *    "This product includes software developed by the OpenSSL Project
 *    for use in the OpenSSL Toolkit (http://www.openssl.org/)"
 *
 * THIS SOFTWARE IS PROVIDED BY THE OpenSSL PROJECT ``AS IS'' AND ANY
 * EXPRESSED OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
 * PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE OpenSSL PROJECT OR
 * ITS CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
 * SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
 * NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 * LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
 * STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
 * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
 * OF THE POSSIBILITY OF SUCH DAMAGE.
 * ====================================================================
 *
 */

#ifndef HEADER_KARM_H
# define HEADER_KARM_H

# include <openssl/opensslconf.h>

# ifdef OPENSSL_NO_KARM
#  error KARM is disabled.
# endif

# include <stddef.h>

# define KARM_ENCRYPT        1
# define KARM_DECRYPT        0

/*
 * Because array size can't be a const in C, the following two are macros.
 * Both sizes are in bytes.
 */

#ifdef  __cplusplus
extern "C" {
#endif

/* This should be a hidden type, but EVP requires that the size be known */

# define KARM_BLOCK_SIZE 16
# define KARM_TABLE_BYTE_LEN 272
# define KARM_TABLE_WORD_LEN (KARM_TABLE_BYTE_LEN / 4)

typedef unsigned int KEY_TABLE_TYPE[KARM_TABLE_WORD_LEN]; /* to match
                                                               * with WORD */

struct karm_key_st {
    union {
        double d;               /* ensures 64-bit align */
        KEY_TABLE_TYPE rd_key;
    } u;
    int grand_rounds;
};
typedef struct karm_key_st KARM_KEY;

# ifdef OPENSSL_FIPS
int private_Karm_set_key(const unsigned char *userKey, const int bits,
                             KARM_KEY *key);
# endif
int Karm_set_key(const unsigned char *userKey, const int bits,
                     KARM_KEY *key);

void Karm_encrypt(const unsigned char *in, unsigned char *out,
                      const KARM_KEY *key);
void Karm_decrypt(const unsigned char *in, unsigned char *out,
                      const KARM_KEY *key);

void Karm_ecb_encrypt(const unsigned char *in, unsigned char *out,
                          const KARM_KEY *key, const int enc);
void Karm_cbc_encrypt(const unsigned char *in, unsigned char *out,
                          size_t length, const KARM_KEY *key,
                          unsigned char *ivec, const int enc);
void Karm_cfb128_encrypt(const unsigned char *in, unsigned char *out,
                             size_t length, const KARM_KEY *key,
                             unsigned char *ivec, int *num, const int enc);
void Karm_cfb1_encrypt(const unsigned char *in, unsigned char *out,
                           size_t length, const KARM_KEY *key,
                           unsigned char *ivec, int *num, const int enc);
void Karm_cfb8_encrypt(const unsigned char *in, unsigned char *out,
                           size_t length, const KARM_KEY *key,
                           unsigned char *ivec, int *num, const int enc);
void Karm_ofb128_encrypt(const unsigned char *in, unsigned char *out,
                             size_t length, const KARM_KEY *key,
                             unsigned char *ivec, int *num);
void Karm_ctr128_encrypt(const unsigned char *in, unsigned char *out,
                             size_t length, const KARM_KEY *key,
                             unsigned char ivec[KARM_BLOCK_SIZE],
                             unsigned char ecount_buf[KARM_BLOCK_SIZE],
                             unsigned int *num);

#ifdef  __cplusplus
}
#endif

#endif                          /* !HEADER_Karm_H */
