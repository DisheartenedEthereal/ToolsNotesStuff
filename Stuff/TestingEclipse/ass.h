/*
 * ass.h
 *
 *  Created on: Dec 22, 2021
 *      Author: meishaden
 */

#ifndef ASS_H_
#define ASS_H_

class ass {
private:
	bool size;
public:
	ass();
	virtual ~ass();
	bool isSize() const;
	void setSize(bool size);
};

#endif /* ASS_H_ */
