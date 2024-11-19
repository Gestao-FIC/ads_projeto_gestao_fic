"use client";

import Link from "next/link";
import { useState } from "react";
import Image from "next/image";
import { Button } from "./ui/button";
import { PiBook, PiChartPieSlice, PiUser } from "react-icons/pi";
import { usePathname } from "next/navigation";
import * as React from "react";
import {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectLabel,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";

const username = "Ana Julia";
const email = "ana.julia@gmail.com";

const NavBar = () => {
  const [activePath, setActivePath] = useState("/");

  const handleLinkClick = (path: string) => {
    setActivePath(path);
  };

  const pathname = usePathname();

  return (
    <>
      {pathname === "/login" ? null : (
        <div className="bg-primary w-52 flex flex-col">
          <div className="p-4 flex flex-col justify-center items-center gap-2">
            <Image
              src="/images/profile-photo.jpg"
              alt="profile-photo"
              width={100}
              height={100}
              className="bg-white rounded-full"
            />
            <p className="text-secondary font-bold">{username}</p>
            <p className="text-secondary font-medium">{email}</p>
            <Link
              href={"/login"}
              className="text-muted-foreground hover:text-muted transition-all ease-in-out font-medium"
            >
              sair
            </Link>
          </div>
          <div className="flex-1 py-10 flex flex-col text-secondary">
            <Link href={"/"} onClick={() => handleLinkClick("/")}>
              <div
                className={`flex flex-row items-center w-full gap-4 px-2 py-1 ${
                  activePath === "/" ? "bg-secondary" : ""
                }`}
              >
                <PiChartPieSlice
                  size={30}
                  color={activePath === "/" ? "black" : "white"}
                />
                <p
                  className={`text-xl ${
                    activePath === "/" ? "text-primary" : "text-secondary"
                  }`}
                >
                  Dashboard
                </p>
              </div>
            </Link>
            <Link
              href={"/docentes"}
              onClick={() => handleLinkClick("/docentes")}
            >
              <div
                className={`flex flex-row items-center w-full gap-4 px-2 py-1 ${
                  activePath === "/docentes" ? "bg-secondary" : ""
                }`}
              >
                <PiUser
                  size={30}
                  color={activePath === "/docentes" ? "black" : "white"}
                />
                <p
                  className={`text-xl ${
                    activePath === "/docentes"
                      ? "text-primary"
                      : "text-secondary"
                  }`}
                >
                  Docentes
                </p>
              </div>
            </Link>
            <Link href={"/cursos"} onClick={() => handleLinkClick("/cursos")}>
              <div
                className={`flex flex-row items-center w-full gap-4 px-2 py-1 ${
                  activePath === "/cursos" ? "bg-secondary" : ""
                }`}
              >
                <PiBook
                  size={30}
                  color={activePath === "/cursos" ? "black" : "white"}
                />
                <p
                  className={`text-xl ${
                    activePath === "/cursos" ? "text-primary" : "text-secondary"
                  }`}
                >
                  Cursos
                </p>
              </div>
            </Link>
          </div>
          <div className="flex justify-center p-4 flex-col gap-2">
            <Select>
              <SelectTrigger className="">
                <SelectValue placeholder="Selecione" />
              </SelectTrigger>
              <SelectContent>
                <SelectGroup>
                  <SelectLabel>Unidade</SelectLabel>
                  <SelectItem value="402">SENAI 402</SelectItem>
                  <SelectItem value="404">SENAI 404</SelectItem>
                </SelectGroup>
              </SelectContent>
            </Select>
            <Button variant={"outline"}>Recarregar</Button>
          </div>
        </div>
      )}
    </>
  );
};

export default NavBar;
